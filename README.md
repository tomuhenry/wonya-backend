# wonya-backend

Deployed App link
[Wonya-Backend](https://wonya-backend.herokuapp.com/)

## Badges

[![codecov](https://codecov.io/gh/tomuhenry/wonya-backend/branch/develop/graph/badge.svg)](https://codecov.io/gh/tomuhenry/wonya-backend) [![Build Status](https://travis-ci.com/tomuhenry/wonya-backend.svg?branch=develop)](https://travis-ci.com/tomuhenry/wonya-backend)

## APIs

### Users

_*User registration*_
`POST /users/registration/`

```
  {
    "username": "testuser",
    "email": "test@test.com",
    "password1": "ujmik,ol.",
    "password2": "ujmik,ol."
  }
```

_*User login*_
`POST /users/login/`

```
  {
    "email": "test@test.com",
    "password": "ujmik,ol."
  }
```

_*User logout*_
`POST /users/logout/`

_*Password Change*_
`POST /users/password/change`

```
  {
    "new_password1": "ujmik,ol.",
    "new_password2": "ujmik,ol."
  }
```

_*Currently logged in user*_
`GET /users/profile`
