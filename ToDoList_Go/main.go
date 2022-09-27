package main

import (
	"fmt"

	"github.com/omoNattie/goToDoList/modules"
)

func main() {
	var choice int
	fmt.Print("1. Create a new task\n2. See your tasks\nEnter here: ")
	fmt.Scan(&choice)

	switch choice {
	case 1:
		modules.CreateTask()

	case 2:
		modules.SeeTasks()

	default:
		panic("That's not a choice..")
	}

}
