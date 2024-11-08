<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/profile">Profile</RouterLink>
    <RouterLink to="/register_login">Register | Login</RouterLink>
  <RouterView />
</template>
