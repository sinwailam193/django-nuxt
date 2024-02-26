<template>
    <div class="py-10 px-6">
        <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
            <h1 class="mb-6 text-2xl">Sign up</h1>
            <form @submit.prevent="handleSubmit">
                <input
                    type="email"
                    placeholder="Your email"
                    class="w-full mb-4 py-4 px-6 rounded-xl"
                    v-model="email"
                />
                <input
                    type="password"
                    placeholder="Your password"
                    class="w-full mb-4 py-4 px-6 rounded-xl"
                    v-model="password"
                />
                <input
                    type="password"
                    placeholder="Confirm password"
                    class="w-full mb-4 py-4 px-6 rounded-xl"
                    v-model="confirmPassword"
                />

                <div
                    v-if="errors.length"
                    class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl"
                >
                    <p v-for="(err, i) in errors" :key="i">
                        {{ err }}
                    </p>
                </div>

                <button
                    type="submit"
                    class="py-4 px-6 bg-teal-700 text-white rounded-xl"
                >
                    Submit
                </button>
            </form>
        </div>
    </div>
</template>

<script setup>
const router = useRouter();
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const errors = ref([]);

async function handleSubmit() {
    errors.value = [];
    try {
        const response = await $fetch('/api/v1/users/', {
            method: 'POST',
            body: {
                username: email.value,
                password: password.value,
            },
        });
        router.push({ path: '/login' });
    } catch (err) {
        if (err.response) {
            for (const key in err.response._data) {
                errors.value.push(`${key}: ${err.response._data[key]}`);
            }
        } else {
            errors.value.push(SERVER_ERROR);
        }
    }
}
</script>
