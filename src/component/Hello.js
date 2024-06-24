// const Hello = () => {
//   <p>Hello</p>
// };
// export default Hello;

import World from "./World"

export default function Hello() {
  // return <p>Hello</p>;
  return (
    <div>
      <p>Hello</p>
      <World />
    </div>
  )
}