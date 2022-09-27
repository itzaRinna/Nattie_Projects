package modules

import (
	"os"
	"os/exec"
	"runtime"
)

func Clear() {
	oss := runtime.GOOS

	switch oss {
	case "linux":
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()

	case "windows":
		cmd := exec.Command("cls")
		cmd.Stdout = os.Stdout
		cmd.Run()

	case "darwin":
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()

	default:
		panic("I can't seem to detect your operating system.....")
	}
}
