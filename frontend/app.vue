<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>

<script setup>
const userStore = useUserStore();

onMounted(() => {
    userStore.initStore();
});
</script>
