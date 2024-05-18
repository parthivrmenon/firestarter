package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

var magicAnswers = [...]string{
	// Positive outcomes
	"It is certain",
	"It is decidedly so",
	"Without a doubt",
	"Yes definitely",
	"You may rely on it",
	"As I see it, yes",
	"Most likely",
	"Outlook good",
	"Yes",
	"Signs point to yes",

	// Neutral outcomes
	"Reply hazy try again",
	"Ask again later",
	"Better not tell you now",
	"Cannot predict now",
	"Concentrate and ask again",

	// Negative outcomes
	"Don't count on it",
	"My reply is no",
	"My sources say no",
	"Outlook not so good",
	"Very doubtful",
}

type Response struct {
	Question string `json:"question"`
	Answer   string `json:"answer"`
}

func rootServiceHandler(w http.ResponseWriter, r *http.Request) {
	response := Response{Question: "None", Answer: "I cannot answer that. Please ask a question."}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)

}

func answerServiceHandler(w http.ResponseWriter, r *http.Request) {
	question := r.URL.Query().Get("question")
	rand.Seed(time.Now().UnixNano())
	answer := magicAnswers[rand.Intn(len(magicAnswers))]
	response := Response{Question: question, Answer: answer}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	fmt.Println("Hello, World!")
	http.HandleFunc("/", rootServiceHandler)
	http.HandleFunc("/ask", answerServiceHandler)
	http.ListenAndServe(":8080", nil)
}
