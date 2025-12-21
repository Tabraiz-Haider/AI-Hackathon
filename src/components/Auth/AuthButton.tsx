import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import Login from './Login';
import Signup from './Signup';
import styles from './AuthButton.module.css';

export default function AuthButton() {
  const { user, logout, isAuthenticated } = useAuth();
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false);

  const handleSwitchToSignup = () => {
    setShowLogin(false);
    setShowSignup(true);
  };

  const handleSwitchToLogin = () => {
    setShowSignup(false);
    setShowLogin(true);
  };

  const handleLogout = () => {
    logout();
    setShowDropdown(false);
  };

  if (isAuthenticated && user) {
    return (
      <div className={styles.userContainer}>
        <button
          className={styles.userButton}
          onClick={() => setShowDropdown(!showDropdown)}
        >
          <span className={styles.userIcon}>👤</span>
          <span className={styles.username}>{user.username}</span>
          <span className={styles.dropdownIcon}>▼</span>
        </button>

        {showDropdown && (
          <div className={styles.dropdown}>
            <div className={styles.dropdownItem}>
              <strong>{user.username}</strong>
              <small>{user.email}</small>
            </div>
            <div className={styles.dropdownDivider} />
            <button className={styles.dropdownButton} onClick={handleLogout}>
              Logout
            </button>
          </div>
        )}
      </div>
    );
  }

  return (
    <>
      <div className={styles.authButtons}>
        <button className={styles.loginButton} onClick={() => setShowLogin(true)}>
          Login
        </button>
        <button className={styles.signupButton} onClick={() => setShowSignup(true)}>
          Sign Up
        </button>
      </div>

      {showLogin && (
        <Login
          onClose={() => setShowLogin(false)}
          onSwitchToSignup={handleSwitchToSignup}
        />
      )}

      {showSignup && (
        <Signup
          onClose={() => setShowSignup(false)}
          onSwitchToLogin={handleSwitchToLogin}
        />
      )}
    </>
  );
}
