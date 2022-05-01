from shapes import PI
print('모듈 이름: {}'.format(__name__))


def circle(radius):
    return PI * radius * radius


def square(length):
    return length * length


def main():
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)
    print(square(2) == 4)
    print(square(5) == 25)


if __name__ == '__main__':
    main()


# __name__  -> 다른 스크립트 or 모듈에서 실행할 경우
# __main__  -> 직접 실행할 경우
