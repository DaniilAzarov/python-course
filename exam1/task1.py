with open("./answer.txt", "w") as output:
    with open("./yazkora.txt", "r") as file:
        line = file.read().replace('\n', ' ').split('.')
        for sentenсe in line:
            if sentenсe.startswith(' '):
                answer = []
                sentense = sentenсe[1:len(sentenсe)]
                words = sentenсe.split()
                for word in words:
                    if word.endswith('yo'):
                        answer.append(word)
                answer = ' '.join(answer) + '\n'
                output.write(answer)
