import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface WorkoutCardProps {
  title: string;
  duration: string;
  intensity: string;
}

export const WorkoutCard: React.FC<WorkoutCardProps> = ({ title, duration, intensity }) => {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.details}>{duration} • {intensity}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    padding: 16,
    marginVertical: 8,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  details: {
    fontSize: 14,
    color: '#38BDF8',
    marginTop: 4,
  },
});
