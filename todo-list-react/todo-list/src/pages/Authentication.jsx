import { Link } from "react-router-dom";
import { useState } from 'react';
import { useCookies } from 'react-cookie';
import '../App.css';

export default function Authentication(){
    const [name, setName] = useState('');
    const [pwd, setPwd] = useState('');
    const [cookies, setCookie, removeCookie] = useCookies(['user']);
    
    const handle = () => {
        setCookie('Name', name, { path: '/' });
        // setCookie('Password', pwd, { path: '/' });
    }

    return (
        <div>
            <div>
                <h1>Who Are You?</h1>
                <input
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div>
                <h1>Password of the user:</h1>
                <input
                    type="password"
                    placeholder="name"
                    value={pwd}
                    onChange={(e) => setPwd(e.target.value)}
                />
            </div>
            <div>
                {/* <Link to="/todo"> */}
                <button className="authBtn" 
                    onClick = {handle}>Register
                </button>
                {/* </Link> */}
                <Link to="/todo">
                <button className="authBtn" 
                    >Login
                </button>
                </Link>
            </div>


                
            <div>
                <button className="authBtn" onClick={() => {
                    removeCookie("Name")
                    }}
                >
                    Delete User Cookies
                </button>
            </div>

            <div className='getCookie'>
                {cookies.Name && (
                  <div className='display'>
                     Current User: <p> {cookies.Name}</p>
                  </div>
                )} 
                {cookies.Password && (
                    <div className='display1'>
                        Password : <p> {cookies.Password}</p>
                    </div>
                )}
            </div>

            <div>
                <Link to="/todo">
                <button className="authBtn">
                    Go to Todo List
                </button>
                </Link>
            </div>
            
        </div>
    );
}