<template>
    <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
        <div class="md:col-span-1 p-6 bg-teal-700 rounded-xl">
            <div class="flex space-x-4">
                <input
                    type="search"
                    placeholder="Find a job..."
                    class="w-full px-6 py-4 rounded-xl"
                />
                <button class="px-6 py-4 bg-teal-900 text-white rounded-xl">
                    <SearchIcon />
                </button>
            </div>
            <hr class="my-6 opacity-30" />
            <h3 class="mt-6 text-xl text-white">Categories</h3>
            <div class="mt-6 space-y-4">
                <p
                    :key="category.id"
                    v-for="category in categories"
                    @click="(event) => toggleCategory(category.id)"
                    class="py-4 px-6 text-white rounded-xl"
                >
                    {{ category.title }}
                </p>
            </div>
        </div>
        <div class="md:col-span-3">
            <div class="space-y-4">
                <!-- <Job />
                <Job />
                <Job /> -->
            </div>
        </div>
    </div>
</template>

<script setup>
const { data: categories } = await useFetch('/api/v1/categories', {
    server: false,
});

const selectedCategory = ref('');
const selectedCategories = {};

function toggleCategory(id) {
    const idSelected = selectedCategories[id];

    if (!idSelected) {
        selectedCategories[id] = true;
    } else {
        delete selectedCategories[id];
    }

    selectedCategory.value = Object.keys(selectedCategories).join(',');
}
</script>
