import { View, Text, TouchableOpacity } from 'react-native';
import React, {useState} from "react"
import LoginForm from '../components/forms/LoginForm';
import SignUpForm from '../components/forms/SignUpForm';

const LandingScreen = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  const handleLogin = () => {
    setShowLogin(true);
    setShowSignup(false);
  };

  const handleSignup = () => {
    setShowSignup(true);
    setShowLogin(false);
  };

  return (
    <View className="flex-1 bg-blue-950 justify-center items-center p-6">
      {!showLogin && !showSignup && (
        <>
          <Text className="text-white text-3xl font-bold mb-8">
            Welcome to Logbook
          </Text>
          <View className="w-full">
            <TouchableOpacity className="bg-white rounded-lg py-3 mb-4" onPress={handleLogin}>
              <Text className="text-blue-950 text-center text-lg font-semibold">
                Login
              </Text>
            </TouchableOpacity>
            <TouchableOpacity className="bg-white rounded-lg py-3" onPress={handleSignup}>
              <Text className="text-blue-950 text-center text-lg font-semibold">
                Signup
              </Text>
            </TouchableOpacity>
          </View>
        </>
      )}
      {showLogin && <LoginForm />}
      {showSignup && <SignUpForm />}
    </View>
  );
};

export default LandingScreen;
