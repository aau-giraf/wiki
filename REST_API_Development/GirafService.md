# Giraf Service

## Description

A service containing helper methods used by many controllers. Additionally it contains the UserManager, Logger and DbContext.

## Helper methods

| Method name | Parameter | Description |
| :---------- | :-------- | :---------- |
| LoadUserWithResources | ClaimsPrincipal | Load user from context, eager load resource fields. Loads all resources. |
| LoadUserWithDepartment | ClaimsPrincipal | Load user from context, eager load resource fields. Loads department resources. |
| LoadUserWithWeekSchedules | string id | Load user from context, eager load resource fields. Loads information related to week schedules. |
| LoadBasicUserDataAsync | ClaimsPrincipal | Loads user from context, does not load resource fields. |
| ReadRequestImage | Stream | Returns a byte array over the image of a pictogram passed through a Stream. |
| CheckPrivateOwnership | Pictogram, GirafUser | Returns a bool determining if the given user owns the Pictogram in question. |
| CheckProtectedOwnership | Pictogram, GirafUser | Returns a bool determining if the given user has access rights through his/hers Department to the Pictogram in question |

## Specifically for LoadUser-methods

When retrieving a user in a controller method it is done with HttpContext.User as parameter:

```Csharp
var usr = await _giraf.LoadUserWithResources(HttpContext.User);
```

## Next

The full [Backend Architexture](./BackendArkitektur.md).