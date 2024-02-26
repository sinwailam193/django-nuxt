<template>
    <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
        <div class="md:col-span-1 p-6 bg-teal-700 rounded-xl">
            <div class="flex space-x-4">
                <input
                    type="search"
                    placeholder="Find a job..."
                    v-model="query"
                    class="w-full px-6 py-4 rounded-xl"
                />
                <button
                    class="px-6 py-4 bg-teal-900 text-white rounded-xl"
                    @click="performSearch"
                >
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
                    :class="{
                        'bg-teal-900': selectedCategories[category.id],
                    }"
                    class="py-4 px-6 text-white rounded-xl"
                >
                    {{ category.title }}
                </p>
            </div>
        </div>
        <div class="md:col-span-3">
            <div class="space-y-4">
                <Job v-for="job in jobs" :key="job.id" :job="job" />
            </div>
        </div>
    </div>
</template>

<script setup>
const queryRef = ref('');
const query = defineModel({ default: '' });

function performSearch() {
    queryRef.value = query.value;
}

const { data: categories } = await useFetch('/api/v1/categories/', {
    lazy: true,
    server: false,
});

const selectedRef = ref('');
const selectedCategories = ref({});

function toggleCategory(id) {
    const idSelected = selectedCategories.value[id];

    if (!idSelected) {
        selectedCategories.value[id] = true;
    } else {
        delete selectedCategories.value[id];
    }

    selectedRef.value = Object.keys(selectedCategories.value).join(',');
}

// it will only retrigger useFetch if using ref
const { data: jobs } = await useFetch('/api/v1/jobs/all/', {
    lazy: true,
    server: false,
    query: {
        query: queryRef,
        categories: selectedRef,
    },
});
</script>
