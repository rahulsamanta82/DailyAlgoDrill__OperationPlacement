export default function MsgBox({username, textcolor}){
    let abc={color: textcolor};
    return <h1 style={abc}>Hello,{username}</h1>
}