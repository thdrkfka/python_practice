import React, {Component} from "react";
/**
 * 클래스형 컴포넌트
 * 1. 상태를 알 수 있는, 데이터/값 을 가진 컴포넌트 => Data 가 있는 내용이므로 class 로 정의
 * 2. 컴포넌트 render() 에는 하나의 태그만 위치
 * 3. default 존재하지 않아도 되나, default가 없으면 중괄호로 import 해줌 => expoert default ~
 */
export class Content extends Component {

  // 상속받은 callback 함수. life cycle hooker
  // 화면에 호출될 때 생성
  render() {
    return (
      <div style='border : 1px solid black;'>
        <h3>클래스형 컴포넌트</h3>
      </div>
    )
  }
}