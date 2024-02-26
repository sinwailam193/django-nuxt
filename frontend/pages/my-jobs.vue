<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My jobs</h1>

        <div v-if="jobs.length" class="space-y-4">
            <Job v-for="job in jobs" :key="job.id" :my="true" :job="job" />
        </div>
    </div>
</template>

<script setup>
const router = useRouter();
const userStore = useUserStore();
const jobs = ref([]);

async function getMyJobs() {
    try {
        const responseJobs = await $fetch('/api/v1/jobs/my/', {
            headers: {
                Authorization: `token ${userStore.user.token}`,
            },
        });

        jobs.value = responseJobs;
    } catch (err) {
        console.error(err.toString());
    }
}

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push({ path: '/login' });
    } else {
        getMyJobs();
    }
});
</script>
