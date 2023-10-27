@echo off

set CGO_ENABLED=1

echo Building your Go DLL...

go build -o draganddrop.dll -buildmode=c-shared main.go

if errorlevel 1 (
    echo Failed to build DLL.
) else (
    echo Successfully built DLL.
)
pause
