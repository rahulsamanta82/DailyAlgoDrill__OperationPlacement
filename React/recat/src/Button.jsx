function hello(){
    console.log("Hi Rahul");
}
export default function Button(){
    return (<div>
        <button onClick={hello}>Click Me !</button>
    </div>)
} 