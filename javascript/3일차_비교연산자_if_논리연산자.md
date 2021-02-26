# 3일차



### 1. 비교 연산자
#### 1.1 비교 연산자

- 비교 연산자는 불린형을 반환한다.

- 문자열을 비교할때, 유니코드 순으로 비교를 하고, 뒤쪽의 문자열 일수록 크다고 생각한다.

- 각 위치별로 비교를 하고, 한쪽이 크면 큰 곳의 값을 반환하고, 종료한다.

- 만약 비교가 종료되었는데도, 동일하고 한쪽 문자열의 길이가 더 길다면, 긴 문자열이 더 크다고 결론 낸다.

  ```javascript
  alert('B'>'C') //false
  alert('BEE'>'BE') //true
  ```

- 만약 **다른형**을 가진 값끼리 비교를 했을 때에는, 이 값들을 숫자형으로 변환 뒤 비교를 한다.

  ```javascript
  alert('2'>1) //true
  alert('0'==0) // true
  alert(true == 0) //false
  ```

- 문자열 `'0'`은 `Boolean`으로 판단시 `false`가 나오지만, 비교연산자로 `0`과 비교시 `true`를 반환한다.

  - 그 이유는 위의 설명과 같이 문자열을 숫자형으로 바꿔서 비교했기 때문이다.

#### 1.2 일치 연산자

- 비교연산자 중 비교 연산자는 `0`과 `false`를 구분하지 못하므로, 좀더 엄격하게 비교를 할때에는 `일치 연산자` 를 사용하여, 값을 비교한다.
- 일치연산자나 불일치연산자(`!==`)를 사용하면, 형변환 없이 값을 비교할 수 있으므로, 좀 더 엄격하게 비교할때 사용이 된다.



#### 1.3  null과 undefined

- `null`과 `undefined`를 일치연산자를 하면, 자료형이 달라서  `false`를 반환하지만, 동등연산자인 `==`를 하면 `true`를 반환한다.

```javascript
alert(null == undefined)  // true
alert(null === undefined )//false
```

- 그러나, 비교연산자를 이용해 `null`은 `0`으로 변환, `undefined`는 `NaN`으로  변환된다.
- `null`과 `undefined`는 동등연산자 `==`일때는 형변환을 하지 않고, 비교연산자인 `>=` ,`>`일때는 형변환을 한다.

```javascript
alert( undefined > 0 ); // false (1)
alert( undefined < 0 ); // false (2)
alert( undefined == 0 ); // false (3)
```

- `undefined`와 `null`은 동등연산자에서 `null`이나 `undefined`가 아니면 `false`를 반환한다.







### 2. if와 `'?'`를 사용한 조건 처리

#### 2.1 `if`문

- if문은 괄호안의 조건을 평가해, 그 결과가 `true`라면 코드 블록을 실행한다.
- `if`문은 괄호안의 조건을 불린값을 변환한다.
  - `0`,`""`,`null`,`undefined`,`NaN` 값은 `false`로 변환, 그 외의 값은 `true`로 반환한다.
- `if`문의 코드블록은 단 한줄이더라도 `{}`중괄호롤 감싸는걸 추천한다.



#### 2.2 else 문

- `else`문은 `if`문 안의 조건이 `false`일 때 실행된다.



#### 2.3 else if 로 복수 조건 처리하기

- 다수의 조건을 처리할 때, `if`문 뒤에 `else if`문을 더 붙여 조건을 판단한다.





#### 2.4 조건부 연산자 `?`

- 조건부 연산자는 `if`문을 좀 더 간결하게 표현가능하다.

  ```javascript
  let result = condition ? value1 ? value2
  // condition이 참이면, value1을 반환, 거짓이면 value2를 반환
  ```



#### 2.5 다중 `?`

```javascript
let result = (condition1) ? value1 : 
(condition2) ? value2 : 
(condition3) ? value3 :
value4;
```

- 위의 예시의 같은 경우 codition1이 참이면 value1, 거짓이면 두번째 `condition2`로 간다.
- `condition2`가 참이면 `value2`를 거짓이면 `condition3`로 간다. 
- `condition3`이 참이면 `value3` 거짓이면 `value4`를 반환한다.

```javascript
if (condition1) {
    result = value1
} else if (condition2){
    result = value2
} else if (condition3) {
    result = value3
} else{
    result = value4
}
```

- 위의 다중 `?`은 다음과 같이 나타낼수 있다.



#### Appendix

- 조건부 연산자 `?`를 남용하지 말고, 조건에 따라 다른 반환값을 할당해야할때만 쓰는 것을 추천한다.





### 3. 논리 연산자

- 논리연산자에는 `||`(OR),`&&`(AND),`!`(NOT)이 있다.
- `OR`와 `AND`는 파이썬과 같은 단축평가를 한다.
- `OR`연산자는 가장 첫번째 `truthly`인 피연산자를 반환하고, 만약 전부 `false`일시에는 마지막 피연산자를 반환한다.

```javascript
alert(""||0||5) //5
alert(""||5||0) //5
```

- `AND`연산자는 `OR`과 반대로 첫번쨰 `falsy`인 피연산자를 찾는다. 첫번쨰 `falsy`인 피연산자를 반환하고, 만약 전부 `true`일 시에는 마지막 피연산자를 반환한다.

```javascript
alert(5&&0&&3) // 0
alert(5&&4&&2) //2
```

- `AND` 연산자가 `OR` 연산자보다 우선순위가 높다.
- `Not`연산자는 느낌표인 `!`을 쓰는데, 먼저 피연산자를 불린형으로 변환후 이에 반대되는 값을 반환해준다.
- 위와 같은 특징을 이용하면, `!!` 와 같이 `Not`연산자를 두개 연속으로 쓸시에는 `Boolean` 함수를 쓴것과 동일한 효과를 나타낸다.
- `Not`은 논리연산자 중 가장 높은 우선순위에 있다.





### 4. null 병합 연산자

-  병합연산자인 ``??``를 사용하면, 짧은 문법으로 그 값이 **확정되어있는** 변수를 찾을수 있다.

  ```javascript
  x = a ?? b
  x = (a !== null && a!== undefined) ? a : b;
  ```

- 위의 두 로직이 같다고 할 수 있다.

- `??`와 `||`(OR)와 비슷하다고 생각할 수 있지만, `||`는 첫번쨰 `truthy` 값을 반환하는데 반해 `??`은 **정의된** 값을 반환하는게 다르다.

```javascript
alert(0 || 100) // 100
alert(0 ?? 100) // 0
```

- `OR`연산자는 숫자 0 은 `false`이므로, 100을 반환해주고, `??`은 연산자는 0이라는 정의되므로, 0을 반환해준다.
- `??`연산자는 `||`와 `&&`연산자와 동시에 사용하는것을 금지한다! 함께 사용시 문법에러가 발생한다.





### 3일차 소감

- 잘 모르던 null 병합연산자와, `?`을 이용한 다중 조건 처리 
- 일치 연산자에서 `null`과 `undefined`의 동작방식에 대해 잘 알 수 있었다.



출처 : [모던 자바스크립트 튜토리얼﻿](https://ko.javascript.info/)









