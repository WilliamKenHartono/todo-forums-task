import { Link } from "react-router-dom";
import '../App.css';
export default function Landing() {
    return (
        <div>
            <h1>Authenticate yourself</h1>
            
            <Link to="/todo">
                <button className="authBtn">Go to Todo List</button>
            </Link>
        </div>
    );
}
