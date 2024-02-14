#문자열 재정렬

data = input()
rslt = [] #알파벳인 경우 별도의 리스트에 저장 - sort() 사용하기 위해서?
val =0

for x in data:
    if x.isalpha(): #리턴값: boolean. cf. isdigit(): 숫자인지 확인하는 함수, 이것 또한 리턴값 불린.
        rslt.append(x) #리스트에 x를 넣기. ㅂ
    else:
        val += int(x) #숫자는 정수형으로 변환해 따로 더하기.(입력 데이터는 문자열임.)
rslt.sort() #알파벳을 오름차순으로 정렬

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if val != 0:
    rslt.append(str(val))

print(''.join(rslt)) # '구분자'.join(리스트명): 리스트를 문자열로 변환하여 출력.
