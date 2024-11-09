<script setup>
import SignIn from '../components/SignIn.vue'
import SignUp from '../components/SignUp.vue'
</script>

<template>
  <div class="auth-container">
    <div class="auth-wrapper">
      <SignIn />
      <div class="divider">
        <span>ИЛИ</span>
      </div>
      <SignUp />
    </div>
  </div>
</template>

<style>
.auth-container {
  max-width: 1280px;
  min-height: 100vh;
  margin: 0 auto;
  padding: 2rem 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  width: 100%;
}

.divider {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  position: relative;
  padding: 0 2rem;
}

.divider span {
  color: #666;
  font-weight: 500;
  position: absolute;
  padding: 0.5rem;
  background: #fff;
  font-size: 1.2rem;
}

.divider::before {
  content: '';
  width: 3px;
  background-color: #ddd;
  height: 100%;
}

.auth-wrapper > *:not(.divider) {
  flex: 1;
  max-width: 50%;
}

@media (max-width: 500px) {
  .auth-wrapper {
    flex-direction: column;
    gap: 2rem;
  }

  .auth-wrapper > *:not(.divider) {
    max-width: 100%;
    width: 100%;
  }

  .divider {
    align-self: stretch;
    padding: 2rem 0;
  }

  .divider::before {
    width: 100%;
    height: 3px;
  }

  .divider span {
    position: absolute;
    background: #fff;
    padding: 0 1rem;
  }
}
</style>
