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
                <p class="py-4 px-6 text-white rounded-xl">Category 1</p>
                <p class="py-4 px-6 text-white rounded-xl">Category 2</p>
                <p class="py-4 px-6 text-white rounded-xl">Category 3</p>
            </div>
        </div>
        <div class="md:col-span-3">
            <div class="space-y-4">
                <Job />
                <Job />
                <Job />
            </div>
        </div>
    </div>
</template>

<script setup></script>
