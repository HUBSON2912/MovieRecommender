import "../css/navigation.css";

export default function NavigationPanel({ children }: { children: React.ReactElement }) {
    return (
        <nav>
            <ul className="navigationPanel">
                {children}
            </ul>
        </nav>
    );
}