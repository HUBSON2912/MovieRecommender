import "../css/navigation.css";

export default function NavigationButton({text}:{text:string}){
    return (
        <li className="navigationButton">{text}</li>
    );
}