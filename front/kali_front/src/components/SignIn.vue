<template>
  <form class="form-signin" @submit="handleSubmit">
    <h1 class="h3 mb-3 font-weight-normal text-center">Войдите</h1>
    <div class="form-group">
      <label for="inputEmail" class="sr-only">Электронная почта</label>
      <input
        type="email"
        id="inputEmail"
        class="form-control"
        placeholder="example@example.ru"
        required
      />
    </div>
    <div class="form-group">
      <label for="inputPassword" class="sr-only">Пароль</label>
      <input 
        type="password" 
        id="inputPassword" 
        class="form-control" 
        placeholder="******" 
        required 
      />
    </div>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Вход</button>
  </form>
</template>

<style scoped>
.form-signin {
  width: 100%;
  max-width: 450px;
  padding: 15px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 8px;
}

.form-control {
  position: relative;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 8px;
  border: 3px solid #ddd;
  transition: border-color 0.2s;
}

.form-control:focus {
  border-color: #ff7518;
  outline: none;
}

.btn {
  width: 25%;
  padding: 10px;
  background-color: #ff7518;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-top: 8px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.btn:active {
  background-color: #e65c00;
}

.text-center {
  text-align: center;
  margin-bottom: 2rem;
}
</style>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const handleSubmit = (event) => {
  event.preventDefault()
  router.push('/profile')
}
</script>
