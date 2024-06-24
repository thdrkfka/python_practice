import React, { Fragment } from "react";

/**
 * 함수형 컴포넌트
 * 1. 상태값이 없는 단순 컴포넌트
 * 2. 파일 하나가 컴포넌트 하ㅏ
 * 3. 파일명 과 컴포넌트 function 명이 같다.
 * 4. 잘 만들어두면 여로곳에서 재사용 가능 => web componenet
 */
export default function Header() {
  return(
    // return 안에 JSX 문법으로 내용 작성
    // return 안에 있는 내용은 상위태그는 하나만 반환
    // => <div> 로 묶어서 반환하는 경우 多
    // <div>
    //   <h2>hi</h2>
    //   <h3>this is react</h3>
    // </div>

    <Fragment>
      <h2>함수형 컴포넌트</h2>
      <h3>this is react</h3>
    </Fragment>
  )
}