<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import UploadZone from './UploadZone.vue'

const router = useRouter()
const isDragging = ref(false)
const selectedFile = ref(null)

const handleSubmit = (event) => {
  event.preventDefault()
  router.push('/profile')
}

const handleDrop = (e) => {
  isDragging.value = false
  const files = e.dataTransfer.files
  if (files.length && files[0].type.startsWith('video/')) {
    selectedFile.value = files[0]
  }
}

const handleFileSelect = (e) => {
  const files = e.target.files
  if (files.length) {
    selectedFile.value = files[0]
  }
}
</script>

<template>
  <div class="form-container">
    <h1 class="h3 mb-3 font-weight-normal text-center">Создайте своё резюме</h1>
    <form class="form-signup">
      <label for="inputFullname" class="sr-only">ФИО</label>
      <input
        type="fullname"
        id="inputFullname"
        class="form-control"
        placeholder="Иванов Иван Иванович"
        required
        autofocus
      />
      <label for="inputEmail" class="sr-only">Электронная почта</label>
      <input
        type="email"
        id="inputEmail"
        class="form-control"
        placeholder="example@example.ru"
        required
        autofocus
      />
      <label for="inputPassword" class="sr-only">Пароль</label>
      <input
        type="password"
        id="inputPassword"
        class="form-control"
        placeholder="******"
        required
      />

      <UploadZone />

      <button class="btn btn-lg btn-primary btn-block button-center" type="submit">
        Зарегистрироваться
      </button>
    </form>
  </div>
</template>

<style scoped>
html,
body {
  height: 100%;
}

body {
  display: -ms-flexbox;
  display: -webkit-box;
  display: flex;
  -ms-flex-align: center;
  -ms-flex-pack: center;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signup {
  width: 100%;
  max-width: 450px;
  padding: 15px;
  margin: 0 auto;
}

.form-signup .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
  margin-bottom: 8px;
  border-radius: 8px;
  border: 3px solid #ddd;
  transition: border-color 0.2s;
}

.form-signup .form-control:focus {
  z-index: 2;
  border-color: #ff7518;
  outline: none;
}

.form-signup input[type='email'] {
  margin-bottom: 8px;
  border-radius: 8px;
}

.form-signup input[type='password'] {
  margin-bottom: 8px;
  border-radius: 8px;
}

.form-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1rem;
}

.btn, .upload-btn {
  cursor: pointer;
  transition: background-color 0.2s;
  background-color: #ff7518;
  border: none;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 8px;
}

.btn:active, .upload-btn:active {
  background-color: #e65c00; /* Немного темнее основного цвета */
}

.video-upload-section {
  margin: rem 0;
}

.video-title {
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 500;
}

.drop-zone {
  border: 3px solid #ddd;
  border-radius: 15px;
  padding: 2rem;
  text-align: center;
  transition: border-color 0.2s;
}

.drop-zone--over {
  border-color: #ff7518;
}

.drop-zone__content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: -8px;
}

.drop-zone__input {
  display: none;
}

.upload-btn {
  background-color: #ff7518;
  color: white;
  padding: 0.75rem 2rem;
  border-radius: 4px;
  cursor: pointer;
}

.upload-btn:hover {
  background-color: #e65c00;
}

.drop-zone__prompt {
  color: #666;
  font-size: 16px;
  margin-bottom: 16px;
}
</style>