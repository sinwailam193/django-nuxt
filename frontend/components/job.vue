<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
            <h3 class="mb-2 text-xl font-semibold">The job position</h3>
            <p class="text-gray-600">The company name</p>
        </div>
        <div>
            <p class="mb-2">Worldwide</p>
            <p>$90-120k</p>
        </div>
        <div>
            <p>Posted Dec. 1st 2024</p>
        </div>
        <div class="space-x-4">
            <NuxtLink
                to="/browse/1 "
                class="py-4 px-6 bg-teal-700 text-white rounded-xl"
            >
                Details
            </NuxtLink>
            <NuxtLink
                v-if="my"
                to="/browse/1 "
                class="py-4 px-6 bg-cyan-700 text-white rounded-xl"
            >
                Edit
            </NuxtLink>
            <NuxtLink
                v-if="my"
                to="/browse/1 "
                class="py-4 px-6 bg-rose-700 text-white rounded-xl"
            >
                Delete
            </NuxtLink>
        </div>
    </div>
</template>

<script setup>
defineProps({
    my: {
        type: [Boolean],
    },
});
</script>
