const API_BASE_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:3000';

export const apiClient = {
  async getWorkouts() {
    const res = await fetch(`${API_BASE_URL}/workouts`);
    return res.json();
  },
  async analyzeFoodImage(imageUri: string) {
    const formData = new FormData();
    formData.append('image', {
      uri: imageUri,
      type: 'image/jpeg',
      name: 'meal.jpg',
    } as any);
    const res = await fetch(`${API_BASE_URL}/nutrition/analyze`, {
      method: 'POST',
      body: formData,
    });
    return res.json();
  },
};
