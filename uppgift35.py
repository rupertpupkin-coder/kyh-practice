import quizzservice

if __name__ == '__main__':
    api = quizzservice.QuizzWebServiceAPI()
    print(f"Antal frågor: {len(api.get_all_questions())}")
    while True:
        print(f"""Det finns {len(api.get_all_questions())} frågor i quiz gör ett val:
    1. Lägg till fråga
    2. Avsluta programmet""")
        answer = input(">>")
        if answer == "2":
            break
        if answer == "1":
            prompt = input("Vad är din fråga?")
            correct = input("Vad är rätt svar?")
            alternatives = input("Ge några felaktiga svar med komma emellan").split(",")
            api.add_question(prompt, correct, alternatives)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
