import React from 'react';
import ReactDOM from 'react-dom/client';
import {Route, BrowserRouter as Router, Routes, Outlet} from 'react-router-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Header from './components/Header';
import Footer from './components/Footer';
import Register from'./components/auth/Register';
import Login from'./components/auth/Login';
import Logout from'./components/auth/Logout';
import Single from'./components/posts/Single';
import Search from'./components/posts/Search';
import Admin from'./Admin';
import Create from'./components/admin/Create';
import Edit from'./components/admin/Edit';
import Delete from'./components/admin/Delete';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
      <Router>
      <Header />
        <Routes>
          <Route path="/" element={<App />} />  
          <Route path="/admin" element={<Admin />} />  
          <Route path="/admin/create" element={<Create />} />  
          <Route path="/admin/edit/:id" element={<Edit />} />  
          <Route path="/admin/delete/:id" element={<Delete />} />  
          <Route path="/register" element={<Register />} />  
          <Route path="/login" element={<Login />} />  
          <Route path="/logout" element={<Logout/>} />  
          <Route path="/post/:slug" element={<Single/>} />  
          <Route path="/search" element={<Search/>} />  
        </Routes>
        <Footer />
      </Router>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
