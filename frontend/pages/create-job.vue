<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Create job</h1>

        <form class="space-y-4" @submit.prevent="handleSubmit">
            <div>
                <label>Category</label>

                <select
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100 after:right-10 after:absolute"
                >
                    <option value="">Select category</option>
                    <option value="dummy1">Category 1</option>
                    <option value="dummy2">Category 2</option>
                </select>
            </div>

            <div>
                <label>Title</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <div>
                <label>Description</label>
                <textarea class="w-full mt-2 p-4 rounded-xl bg-gray-100" />
            </div>

            <div>
                <label>Salary</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <div>
                <label>location</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <div>
                <label>Company name</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <div>
                <label>Company location</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <div>
                <label>Company email</label>
                <input
                    type="text"
                    class="w-full mt-2 p-4 rounded-xl bg-gray-100"
                />
            </div>

            <button
                type="submit"
                class="py-4 px-6 bg-teal-700 text-white rounded-xl"
            >
                Submit
            </button>
        </form>
    </div>
</template>

<script setup>
const router = useRouter();
const userStore = useUserStore();

async function handleSubmit() {}

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push({ path: '/login' });
    }
});
</script>
