# Challenge

So Santa wanted to launch a lottery service on the North Pole. Can you have a *look* and see if you can win?

http://santaslottery.norwayeast.azurecontainer.io/

> **Hint:** How do PRNGs work again?

# Writeup

Hint and most of it goes to that there is a psudo random generator. Those er often predictable but not easy unless we know some seed or anything.

But checking the source code it seems to be running the same .net app as in a earlier task. And the form contains an UUID4 which is changed on every refresh. Is this the seed for dotnet's PRnG? Or indicator for time? 

Googling "dotnet random int64" I get the documentation for dotnet's [Random.NextInt64](https://learn.microsoft.com/en-us/dotnet/api/system.random.nextint64?view=net-6.0) and I'm stoked. That is it.

Asking ChatGPT to write me a dotnet script: "Create a dotnet script to get a random int64 based on a given seed"

```
using System;

public class Program
{
    public static void Main()
    {
        // Replace 12345 with your desired seed value
        int seed = 12345;
        Random rnd = new Random(seed);
        long randomInt64 = rnd.NextInt64();
        Console.WriteLine(randomInt64);
    }
}
```

I'm in. I've never written dotnet and dont know how to compile it  but I quicky found [dotnet fiddle](https://dotnetfiddle.net/) and selected the newest dotnet 7 version. Pasted the code and there it spits out a number. Changing the seed changes the number. So I'll try to input the seed in the html form. The UUID4.

```
Compilation error (line 8, col 20): Cannot implicitly convert type 'string' to 'int'
```

Mkey, I google how to make uuid a int I get two different methods:

```
int i = Guid.NewGuid().GetHashCode();

int j = BitConverter.ToInt32(Guid.NewGuid().ToByteArray(), 0);
```

I tried both but no luck, I then continue to search and use different methods and this goes on a bit of trial and error a few hours until suddenly I see the image creation date. ?`2022:12:20 20:21:39+01:00`. I do my jolly cheer and am so happy. That must be the seed, converted to epoc time. That uuid4 is possible just a decoy..

Converting and having fun, but no.. Bust again. Back to uuid to int on google.

So I'm stuck here:

```C#
using System;

// Generate a new string
string seedString = "3dc4c432-9b99-42a0-8a77-abb5fa409c7e";

// Get the hash code of the string
int seed = seedString.GetHashCode();

// Create a new Random object with the seed
Random rand = new Random(seed);

// Generate a random 64-bit integer
long randomInt = rand.NextInt64();

Console.WriteLine(randomInt);
```

Little did I know I was SO close.. So a few hours of looking around I luckily have the inspector up on the browser while just testing random numbers.. What, is that a comment under the error in the error page?

```
<!-- Tests broke every time we ran this, so I discovered this about .NET Core: https://andrewlock.net/why-is-string-gethashcode-different-each-time-i-run-my-program-in-net-core/ It was very helpful! Now the tests all pass! -->
```

I quickly printout the hash and see, damn it changes every time! I thought it was static. But this website shows how to generate a static one by adding our own hashing function. So I implement what I understand to my above script:

```c#
using System;
			
string seedString = "d9e2084d-a260-4c69-a625-040f2d60ed36";

int hash1 = (5381 << 16) + 5381;
int hash2 = hash1;

for (int i = 0; i < seedString.Length; i += 2)         {
	hash1 = ((hash1 << 5) + hash1) ^ seedString[i];
	if (i == seedString.Length - 1)
		break;
	hash2 = ((hash2 << 5) + hash2) ^ seedString[i + 1];
}
int seed = hash1 + (hash2 * 1566083941);

// Create a new Random object with the seed
Random rand = new Random(seed);

// Generate a random 64-bit integer
long randomInt = rand.NextInt64();

Console.WriteLine(randomInt);
```

And there it goes:

```
We Have a Winner!

Wov that truly was 1 in 9.223372036854775807 × 1018

Here is your prize:

${W3_4@V3_@_V3RY_1UCKY_B@57@RD!}
```