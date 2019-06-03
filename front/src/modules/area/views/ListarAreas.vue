<template>
    <v-container fluid>
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <v-data-table
                    :headers="header"
                    :items="areas"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            {{ props.item.localidade }}
                        </td>
                        <td>
                            {{ props.item.dimensao }}
                        </td>
                        <td>
                            {{ props.item.largura }} x {{ props.item.comprimento }}
                        </td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="visualizar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    grid_on
                                </v-icon>
                                {{ props.item.nome }}
                            </v-btn>
                        </td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="editar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    edit
                                </v-icon>
                                editar
                            </v-btn>
                            <v-btn
                                flat
                                small
                                @click="excluir(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    clear
                                </v-icon>
                                excluir
                            </v-btn>
                        </td>
                    </template>
                </v-data-table>
                <v-btn
                    dark
                    class="green darken-1"
                    @click="adicionar()"
                >
                    <v-icon
                        white
                        class="pr-2">
                        add
                    </v-icon>
                    adicionar área
                </v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarAreas',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'center',
                    sortable: false,
                    value: 'numero',
                },
                {
                    align: 'center',
                    text: 'localidade',
                    value: ' localidade',
                },
                {
                    align: 'center',
                    text: 'dimensao',
                    value: ' dimensao',
                },
                {
                    align: 'center',
                    text: 'largura x comprimento',
                    value: ' comprimento',
                },
                {
                    align: 'center',
                    text: 'nome',
                    value: 'nome',
                },
                {
                    align: 'center',
                    text: 'ações',
                    value: 'acoes',
                },
            ],
            areas: [],
        };
    },
    computed: {
        ...mapGetters({
            listaAreas: 'area/areas',
        }),
    },
    watch: {
        listaAreas() {
            this.areas = this.listaAreas;
        },
    },
    created() {
        this.buscarAreas();
    },
    methods: {
        ...mapActions({
            buscarAreas: 'area/buscarAreas',
        }),
        visualizar(id) {
            const path = `/area/${id}`;
            this.$router.push({ path });
        },
        editar(id) {
            const path = `/area/${id}/edit`;
            this.$router.push({ path });
        },
        adicionar() {
        },
        excluir(id) {
        },
    },
};
</script>
