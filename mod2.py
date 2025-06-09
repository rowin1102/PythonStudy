def mul(a, b):
  return a * b

def div(a, b):
  return a / b

""" __name__  변수 : 파이썬 내부에서 사용하는 특별한 변수로 해당 파일을 콘솔에서 직접
  실행하면 '__main__'이라는 문자열이 저장된다. 
  하지만 import하는 경우에는 모듈의 이름, 즉 mod2가 저장된다."""
if __name__ == '__main__':
  print('==여긴 mod2.py==')
  print(mul(1, 4))
  print(div(4, 2))