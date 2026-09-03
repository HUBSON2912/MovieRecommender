import "../css/navigation.css";

export default function NavigationPanel({ children }: { children: React.ReactElement }) {
    return (
        <nav className="navigationPanel">
            {children}
        </nav>
    );
}