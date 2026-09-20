import { NestFactory } from '@nestjs/core';
import { Module } from '@nestjs/common';
import { WorkoutsController } from './modules/workouts.controller';

@Module({
  controllers: [WorkoutsController],
})
export class AppModule {}

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors();
  const port = process.env.PORT || 3000;
  await app.listen(port);
  console.log(`FitFlow Backend is running on: http://localhost:${port}`);
}
bootstrap();
