from drugstore import app


@app.task
def enter_log(text):
    from time import sleep
    sleep(30)
    with open('log.log', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


@app.task
def spam_attack():
    with open('spam.log', 'a') as file:
        file.write('spam\n')
