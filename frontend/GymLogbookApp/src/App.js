import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import LandingScreen from './screens/LandingScreen';
import AppNavigator from './navigation/AppNavigator';

export default function App() {
  return (
      <AppNavigator/>
  );
}

