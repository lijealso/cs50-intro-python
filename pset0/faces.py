def convert(sentence_output):
    sentence_output = sentence_output.replace(":)", "🙂").replace(":(", "🙁")
    return sentence_output

def main():
    sentence = input("Enter sentence: ")
    print(convert(sentence))

main()