import { Controller, Get, Post, Body, UseGuards } from '@nestjs/common';
import { FirebaseAuthGuard } from '../auth/firebase-auth.guard';

@Controller('workouts')
export class WorkoutsController {
  @Get()
  getWorkouts() {
    return [
      { id: '1', title: 'Full Body HIIT', duration: '30 mins', intensity: 'High' },
      { id: '2', title: 'Strength & Core', duration: '45 mins', intensity: 'Moderate' },
    ];
  }

  @Post('generate-daily')
  @UseGuards(FirebaseAuthGuard)
  generateDailyWorkout(@Body() body: { fatigueLevel: number; goal: string }) {
    return {
      message: 'Workout generated successfully via AI service',
      plan: {
        title: 'Adaptive Flow Recovery',
        duration: '25 mins',
        exercises: ['Dynamic Warmup', 'Mobility Stretches', 'Light Core'],
      },
    };
  }
}
