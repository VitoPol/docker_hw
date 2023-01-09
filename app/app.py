import redis

client = redis.Redis(host="redis", port=6379)

if __name__ == '__main__':
    while True:
        user_input = input(">>> Введите пример: ")
        if user_input.lower() == "stop":
            break
        client.lpush("queue", user_input)
