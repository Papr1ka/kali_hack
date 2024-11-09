<style scoped>
.root {
    --p-button-primary-background: #ff7518;
    border: 0px;   
}

.p-fileupload-choose:active {
  background-color: #e65c00 !important; /* Немного темнее основного цвета */
}
</style>

<template>
    <div class="upload-container">
        <Toast />
        <FileUpload name="demo[]" url="/api/upload" @upload="onAdvancedUpload($event)"
        :multiple="true" accept="image/*" :maxFileSize="1000000">
            <template #empty>
                <span>Перетащите файлы сюда для загрузки</span>
            </template>
        </FileUpload>
    </div>
</template>

<script setup>
import FileUpload from 'primevue/fileupload';
import { useToast } from "primevue/usetoast";
const toast = useToast();

const onAdvancedUpload = () => {
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
};
</script>