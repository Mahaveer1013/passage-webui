# passage-webui
webui for gopass

	The project is handled using `uv`

## Initiate password store
- Install age (Used for encryption)
```
sudo apt install age
```
  - use your package manager to install age or download the binaries from the official github (https://github.com/FiloSottile/age)
- Generate a keygen
```
mkdir $HOME/.passage
age-keygen -o $HOME/.passage/identities
```
- If it is successful, identities file will be generate and sample content will be like this
```
# created: 2025-02-22T22:56:49+05:30
# public key: age15luhzckhsr9mfk2m9f3t0hxk97j4sazt6ajmptl8vegz9kzpg36slg6xek
AGE-SECRET-KEY-1KQJSZ96HKR2XU0UN9KM7WR7PAXR9FTM836J790VQ70GV0P3WPDGQV37UW0
```
- Download the [password-store.sh](https://github.com/FiloSottile/passage/blob/main/src/password-store.sh) file
- When you execute the script you should get the following error
```
 ./password-store.sh
Error: password store is empty.
```
- Adding password
```
./password-store.sh add personal/helloking@gmail.com
```
- Accessing password
```
./password-store.sh personal/helloking@gmail.com
```
- Adding a account with random password
```
./password-store.sh generate personal/helloking@gmail.com
The generated password for personal/helloking@gmail.com is:
DpW)wr2'Y63jL[!7PM)<wVBXL
```
- Install the passage
```
sudo make install
```
- Once installed you can access the passage using passage command
## Run the project in debug mode
```
uv run fastapi dev main.py
```

## Built on the using of
- [Passage](https://github.com/FiloSottile/passage)
- HTMX
- FastAPI
- FontAwesome

## Screenshots

![Homepage](./image/image1.png)
![NewPassword](./image/image2.png)
![Settings](./image/image3.png)
![Homepage2](./image/image4.png)

## Reference blog, link for the projects
- How to send html file from fast api
  - https://stackoverflow.com/questions/65916537/a-minimal-fastapi-example-loading-index-html
- HTMX: https://htmx.org/

