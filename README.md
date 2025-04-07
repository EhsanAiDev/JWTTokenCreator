# JWTTokenCreator

JWTTokenCreator is a simple command-line tool for generating JSON Web Tokens (JWT) signatures using HMAC (Hash-based Message Authentication Code) with specified hashing algorithms. This tool allows users to create a JWT by providing a header and payload, a secret key, and the desired hashing algorithm.

## Features

- Supports multiple hashing algorithms: SHA-256, SHA-384, and SHA-512.
- Generates a JWT signature based on the provided header and payload.
- Outputs the complete JWT in the format: `header.payload.signature`.

## Requirements

- Python 3.x
- Standard libraries: `argparse`, `hmac`, `base64`, `hashlib`

## Usage

To use JWTTokenCreator, run the script from the command line with the following arguments:

```bash
python jwt_token_creator.py -hp <header.payload> -s <secret_key> -alg <algorithm>
```
## Arguments
  -hp: (required) The header and payload value in the format header.payload. This should be a base64url encoded string.
  
  -s: (required) The secret key used for signing the JWT.
  
  -alg: (required) The algorithm used for the signature. Choose from the following options:
      SHA-256
      SHA-384
      SHA-512

## Example
```bash
python jwt_token_creator.py -hp "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ" -s "your-256-bit-secret" -alg "SHA-256"
```
This command will output a JWT in the format:
```Code

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.<signature>
```
