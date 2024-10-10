import { View, Text, TouchableOpacity } from 'react-native';
import React, {useState} from "react"


const LandingScreen = ({navigation}) => {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  return (
    <View className="flex-1 bg-blue-950 justify-center items-center p-6">
          <Text className="text-white text-3xl font-bold mb-8">
            Welcome to Logbook
          </Text>
          <View className="w-full">
            <TouchableOpacity className="bg-white rounded-lg py-3 mb-4" onPress={()=> navigation.navigate('Login')}>
              <Text className="text-blue-950 text-center text-lg font-semibold">
                Login
              </Text>
            </TouchableOpacity>
            <TouchableOpacity className="bg-white rounded-lg py-3" onPress={()=> navigation.navigate('Signup')}>
              <Text className="text-blue-950 text-center text-lg font-semibold">
                Signup
              </Text>
            </TouchableOpacity>
          </View>
    </View>
  );
};

export default LandingScreen;
