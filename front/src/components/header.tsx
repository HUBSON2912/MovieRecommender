import NavigationPanel from "./navigationPanel";
import NavigationButton from "./navigationButton";
import "../css/header.css";

export default function Header() {
    return (
        <header className="header">
            <h1 className="title">
                MovieRecomender
            </h1>
            <NavigationPanel>
                <>
                    <NavigationButton text="search" />
                    <NavigationButton text="rated" />
                    <NavigationButton text="recommendations" />
                    <NavigationButton text="about" />
                </>
            </NavigationPanel>
        </header>
    );
}