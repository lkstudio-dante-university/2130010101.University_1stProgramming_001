import os
import sys

"""
Python 변수 종류
- 지역 변수
- 전역 변수

지역 변수 vs 전역 변수
- 지역 변수는 특정 영역에 속해있는 변수를 의미하며 해당 변수가 선언 된 지역 내부에서만 사용 할 수 있다는 특징이 존재한다. 반면, 전역 변수는
특정 영역에 속해 읺지 않은 변수를 의미하며 프로그램 전체에서 사용 가능하다는 차이점이 존재한다. (즉, 지역 변수는 해당 변수가 선언 된 영역을
벗어나면 사라지는 특징이 있다는 것을 알 수 있다.)

Python 에서 특정 지역 (영역) 은 : (콜론) 기호로 시작한다. (즉, 해당 기호 하위에 선언 된 변수 또는 매개 변수는 지역 변수라는 것을 의미한다.)

Python 변수 선언 방법
- 변수 이름 + 자료형 (옵션) + 초기화 데이터

Ex)
nVal = 0
nVal: int = 0

Python 은 강력 형식 언어 (Strong Type Language) 가 아니기 때문에 자료형을 명시하지 않고 변수를 선언하는 것이 가능하다.
(즉, Python 은 변수가 관리하는 데이터의 자료형을 제한하지 않는다는 것을 알 수 있다.)

단, Python 은 변수에 자료형을 명시하는 기능을 제공하며 해당 기능을 활용하면 에디터의 인텔리센스 기능의 도움을 받는 것이 가능하다.
(즉, 지역 변수나 매개 변수는 초기화 데이터를 통해 에디터가 해당 변수의 자료형을 유추하는 것이 가능하지만 매개 변수는 초기화 데이터가 존재하지
않기 때문에 자료형을 명시하지 않으면 에디터의 인텔리센스 기능이 동작하지 않는다.)

Python 은 변수 이름을 비롯한 특정 대상의 이름을 작성 할 때에는 알파벳 대/소문자, _ (언더 스코어), 숫자만 사용하는 것을 추천한다. (즉, 일부
특수 문자를 제외한 여러 문자를 통해 이름을 작성하는 것이 가능하지만 대부분의 언어가 알파벳만을 지원하기 때문에 이를 따르는 것이 좋은 선택이라는
것을 알 수 있다.)

또한, 이름의 첫 문자는 숫자가 될 수 없다는 특징이 존재한다.

Ex)
nVal01 = 0
01nVal = 0

위의 경우 nVal01 이름은 사용하는 것이 가능하지만 01nVal 은 첫 문자로 숫자로 시작하기 때문에 사용하는 것이 불가능하다.

연산자란?
- 프로그램이 동작하는데 특별한 역할을 수행하는 기호 (심볼) 을 의미한다. (즉, 연산자를 활용하면 특정 데이터를 프로그램의 목적에 맞게 처리하는
것이 가능하다는 것을 알 수 있다.)

Python 은 피연산자를 1 개 요구하는 단항 연산자와 피연산자를 2 개 요구하는 이항 연산자를 지원한다. 또한, 연산자는 한 라인에 중첩으로 작성하는
것이 가능하며 한 라인에 중첩으로 작성 된 연산자는 우선 순위에 따라 처리 순서가 결정된다.

Ex)
2 + 2 * 2		<- 6
(2 + 2) * 2		<- 8

* (곱하기 연산자) 는 + (더하기 연산자) 보다 우선 순위가 높기 때문에 먼저 처리 된다는 것을 알 수 있다. 이때, 연산자의 처리 순서를 변경하고
싶다면 ( ) (우선 순위 연산자) 를 명시해주면 된다.

Python 연산자 종류
- 산술 연산자 (+, -, *, /, %, **, //)
- 관계 연산자 (<, >, <=, >=, ==, !=)
- 할당 연산자 (=, +=, -=, *=, /=, 등등...)
- 논리 연산자 (and, or, not)
- 비트 연산자 (&, |, ^, <<, >>, ~)
- 기타 연산자 (우선 순위 연산자, 함수 호출 연산자 등등...)

관계 연산자란?
- 데이터의 대/소 여부를 판단하기 위한 연산자를 의미한다. (즉, 해당 연산자의 결과는 참 or 또는 거짓을 나타내는 bool 형 데이터가
반환된다는 것을 알 수 있다.)

할당 연산자란?
- 우항에 명시 된 데이터를 좌항에 명시 된 변수에 저장하는 연산자를 의미한다. (즉, 특정 변수에 데이터를 저장하기 위해서는 할당 연산자를
활용하면 된다는 것을 알 수 있다.)

비트 연산자란?
- 프로그래밍 언어의 기본 단위는 바이트이기 때문에 대부분의 연산자는 바이트 단위로 동작하는 특징이 존재한다. 반면, 비트 연산자는 비트 단위로
데이터를 제어하는 것이 가능하다. (즉, 비트 단위로 데이터를 제어함으로서 프로그램이 사용하는 메모리를 최소화 시키는 것이 가능하다.)
"""


# Example 10
def Example_10(args):
	# Example_10_01(args)
	# Example_10_02(args)
	Example_10_03(args)


g_nGlobalVal = 0


# Example 10 - 1
def Example_10_01(args):
	"""
	Python 은 변수의 선언과 사용이 명확하게 구분되지 않기 때문에 특정 변수를 사용 할 때 이를 주의해야한다. (즉, 특정 변수의 값을 가져오는
	것은 항상 변수의 사용에 해당하지만 특정 변수에 값을 저장하는 행위는 선언과 사용 모두 해당한다는 것을 알 수 있다.)
	
	특정 변수에 값을 할당 할 경우 이는 변수 선언에 해당하며 이미 선언 된 변수에 값을 할당하는 것은 변수의 사용에 해당한다.
	"""
	nVal = 10
	fVal = 3.14
	bIsTrue = True
	
	"""
	global 키워드는 전역 변수를 사용하겠다는 것을 알리는 역할을 수행한다. (즉, 해당 키워드를 사용하지 않고 전역 변수에 값을 할당 할 경우
	이는 전역 변수의 사용이 아니라 전역 변수와 동일한 이름을 지니는 지역 변수의 선언에 해당한다는 것을 알 수 있다.)
	
	Python 은 특정 지역이 항상 전역보다 우선 순위가 높기 때문에 특정 지역에서 전역 변수를 사용하기 위해서는 반드시 global 키워드를 명시해
	줘야한다.
	"""
	global g_nGlobalVal
	g_nGlobalVal = 10
	
	"""
	변수 이름을 명시하는 것은 해당 변수에 저장 된 데이터를 가져오는 것을 의미한다. (즉, 정수 10 이 저장 된 특정 변수가 있을 경우 해당 변수에
	저장 된 10 이라는 값을 가져오고 싶다면 해당 변수의 이름을 명시하면 된다는 것을 알 수 있다.)
	
	단, 선언 되지 않은 변수를 명시 할 경우 런타임 에러가 발생하기 때문에 변수의 데이터를 가져오는 것은 주의가 필요하다. (즉, 변수의 데이터를
	가져오는 과정에서 에러가 발생한다면 해당 변수가 선언 된 변수인지 먼저 확인 할 필요가 있다는 것을 알 수 있다.)
	
	문자열 포맷팅이란?
	- 문자열의 일부 or 전체를 특정 데이터롤 치환해서 문자열 데이터를 생성 할 수 있는 기능을 의미한다. (즉, 문자열 포맷팅을 활용하면 변수 등을
	사용해서 원하는 문장을 자유롭게 구성 할 수 있다는 것을 알 수 있다.)
	
	Python 문자열 포맷팅 사용 방법
	- 서식 문자를 포함하고 있는 문자열 데이터 + 데이터
	
	Ex)
	"{0}, {1}".format(10, 20)					<- "10, 20" 문자열 데이터 생성
	"{0} + {1} = {2}".format(10, 20, 10 + 20)	<- "10 + 20 = 30" 문자열 데이터 생성
	
	Python 서식 문자는 { } 와 번호 조합을 통해 명시하는 것이 가능하다. (즉, 번호는 format 메서드에 전달 되는 데이터의 순서를 의미한다는
	것을 알 수 있다.)
	
	단, 서식 문자 번호는 1 이 아니라 0 부터 시작하기 때문에 주의가 필요하다.
	"""
	print("=====> 값 형식 자료형 <=====")
	print("{0}, {1}".format(nVal, type(nVal)))
	print("{0}, {1}".format(fVal, type(fVal)))
	print("{0}, {1}".format(bIsTrue, type(bIsTrue)))
	
	oStr = "Hello, World!"
	oList = [1, 2, 3, 4, 5]
	oDict = {"Key_01": 1, "Key_02": 2, "Key_03": 3, "Key_04": 4, "Key_05": 5}
	oTuple = (1, 2, 3, 4, 5)
	
	print("\n=====> 참조 형식 자료형 <=====")
	print("{0}, {1}".format(oStr, type(oStr)))
	print("{0}, {1}".format(oList, type(oList)))
	print("{0}, {1}".format(oDict, type(oDict)))
	print("{0}, {1}".format(oTuple, type(oTuple)))


# Example 10 - 2
def Example_10_02(args):
	nLocalVal = 10
	global g_nGlobalVal
	
	g_nGlobalVal = 20
	
	print("=====> 지역 변수 및 전역 변수 - 1 <=====")
	print("지역 변수 : {0}".format(nLocalVal))
	print("전역 변수 : {0}".format(g_nGlobalVal))


# Example 10 - 3
def Example_10_03(args):
	"""
	nLocalVal 변수는 Example_10_02 메서드 하위에 속해있는 지역 변수이기 떄문에 해당 지역을 벗어난 외부에서는 접근이 불가능하다.
	반면, g_nGlobalVal 변수는 전역 변수이기 때문에 프로그램 어디서든 접근 가능하다는 것을 알 수 있다.
	"""
	print("=====> 지역 변수 및 전역 변수 - 2 <=====")
	# print("지역 변수 : {0}".format(nLocalVal))
	print("전역 변수 : {0}".format(g_nGlobalVal))
	
	"""
	input 메서드란?
	- 콘솔 창으로부터 데이터를 입력 받을 수 있는 메서드를 의미한다. (즉, 해당 메서드를 활용하면 프로그램이 실행 중에 사용자로부터 특정
	데이터를 입력받는 것이 가능하다.)
	
	단, input 메서드는 콘솔 창으로부터 입력 받은 데이터를 문자열 데이터로 반환하기 때문에 정수 or 실수와 같은 숫자 데이터를 입력 받기 위해서는
	문자열 데이터를 숫자 데이터로 변환하는 추가적인 연산이 필요하다.
	"""
	oTokenList = input("\n정수 (2 개) 입력 : ").split()
	
	"""
	문자열 데이터를 정수 or 실수 데이터로 변환하기 위해서는 해당 자료형을 명시해주면 된다.
	
	Ex)
	int("10")		<- 문자열 10 을 정수 10 으로 변환
	float("3.14")	<- 문자열 3.14 를 실수 3.14 로 변환
	"""
	nVal01 = int(oTokenList[0])
	nVal02 = int(oTokenList[1])
	
	print("=====> 산술 연산자 <=====")
	print("{0} + {1} = {2}".format(nVal01, nVal02, nVal01 + nVal02))
	print("{0} - {1} = {2}".format(nVal01, nVal02, nVal01 - nVal02))
	print("{0} * {1} = {2}".format(nVal01, nVal02, nVal01 * nVal02))
	print("{0} / {1} = {2}".format(nVal01, nVal02, nVal01 / nVal02))
	print("{0} % {1} = {2}".format(nVal01, nVal02, nVal01 % nVal02))
	print("{0} ** {1} = {2}".format(nVal01, nVal02, nVal01 ** nVal02))
	print("{0} // {1} = {2}".format(nVal01, nVal02, nVal01 // nVal02))
	
	"""
	관계 연산자 or 논리 연산자는 결과 값으로 참 or 거짓을 반환한다. (즉, bool 자료형 데이터를 연산 결과로 반환한다는 것을 알 수 있다.)
	"""
	print("\n=====> 관계 연산자 <=====")
	print("{0} < {1} = {2}".format(nVal01, nVal02, nVal01 < nVal02))
	print("{0} > {1} = {2}".format(nVal01, nVal02, nVal01 > nVal02))
	print("{0} <= {1} = {2}".format(nVal01, nVal02, nVal01 <= nVal02))
	print("{0} >= {1} = {2}".format(nVal01, nVal02, nVal01 >= nVal02))
	print("{0} == {1} = {2}".format(nVal01, nVal02, nVal01 == nVal02))
	print("{0} != {1} = {2}".format(nVal01, nVal02, nVal01 != nVal02))
	
	print("\n=====> 논리 연산자 <=====")
	print("{0} and {1} = {2}".format(nVal01, nVal02, nVal01 and nVal02))
	print("{0} or {1} = {2}".format(nVal01, nVal02, nVal01 or nVal02))
	print("not {0} = {1}".format(nVal01, not nVal01))
	
	"""
	^ 연산자는 XOR 연산자이다. (즉, 해당 연산자는 좌항과 우항이 서로 다른 경우 참이며 좌항과 우항이 같을 경우 거짓이 된다는 것을 알 수 있다.)
	"""
	print("\n=====> 비트 연산자 <=====")
	print("{0:08b} & {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 & nVal02))
	print("{0:08b} | {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 | nVal02))
	print("{0:08b} ^ {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 ^ nVal02))
	print("{0:08b} << 1 = {1:08b}".format(nVal01, nVal01 << 1))
	print("{0:08b} >> 1 = {1:08b}".format(nVal02, nVal02 >> 1))
	print("~{0:08b} = {1:08b}".format(nVal01, ~nVal01 + 1))
